import torch
import torch.nn as nn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from backend.selling.repository import get_quote_closes_values

quote_close_values = get_quote_closes_values()
print(quote_close_values)

test_data_size = 60  # кол-во 5-минуток на которые мы делаем прогноз
train_data = quote_close_values[:-test_data_size]
test_data = quote_close_values[-test_data_size:]

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(-1, 1))  # нормализация данных на промежуток (-1;1)
train_data_normalized = scaler.fit_transform(train_data).reshape(-1, 1)

print(train_data_normalized[:5])
print(train_data_normalized[-5:])

train_data_normalized = torch.FloatTensor(train_data_normalized).view(-1)  # преобразование нормализованного ..
# .. датасета в тензоры

train_window = 12  # периодичность последовательность (мы взяли 12 так как это 1ч/5мин)


# создает список картежей в каждом кортеже будут данные за 1 час и данные за след. час
def create_inout_sequences(input_data, train_w):
    inout_seq = []
    input_data_length = len(input_data)
    for i in range(input_data_length - train_w):
        train_seq = input_data[i:i + train_w]
        train_label = input_data[i + train_w:i + train_w + 1]
        inout_seq.append((train_seq, train_label))
    return inout_seq


train_inout_seq = create_inout_sequences(train_data_normalized, train_window)


# train_inout_seq[:5]


class LSTM(nn.Module):
    def __init__(self, input_size=1, hidden_layer_size=1000, output_size=1):
        super().__init__()
        self.hidden_layer_size = hidden_layer_size

        self.lstm = nn.LSTM(input_size, hidden_layer_size)

        self.linear = nn.Linear(hidden_layer_size, output_size)

        self.hidden_cell = (torch.zeros(1, 1, self.hidden_layer_size),
                            torch.zeros(1, 1, self.hidden_layer_size))

    def forward(self, input_seq):
        lstm_out, self.hidden_cell = self.lstm(input_seq.view(len(input_seq), 1, -1), self.hidden_cell)
        predictions = self.linear(lstm_out.view(len(input_seq), -1))
        return predictions[-1]


model = LSTM()
loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)

print(model)

epochs = 2
single_loss = None
for i in range(epochs):
    for seq, labels in train_inout_seq:
        optimizer.zero_grad()
        model.hidden_cell = (torch.zeros(1, 1, model.hidden_layer_size),
                             torch.zeros(1, 1, model.hidden_layer_size))

        y_pred = model(seq)

        single_loss = loss_function(y_pred, labels)
        single_loss.backward()
        optimizer.step()

    if i % 25 == 1:
        print(f'epoch: {i:3} loss: {single_loss.item():10.8f}')

    print(f'epoch: {i:3} loss: {single_loss.item():10.10f}')

fut_pred = 12

test_inputs = train_data_normalized[-train_window:].tolist()
print(test_inputs)

model.eval()

for i in range(fut_pred):
    seq = torch.FloatTensor(test_inputs[-train_window:])
    with torch.no_grad():
        model.hidden = (torch.zeros(1, 1, model.hidden_layer_size),
                        torch.zeros(1, 1, model.hidden_layer_size))
        test_inputs.append(model(seq).item())

# test_inputs[fut_pred:]

actual_predictions = scaler.inverse_transform(np.array(test_inputs).reshape(-1, 1))
print(actual_predictions)

elems_count = len(quote_close_values)
x = np.arange(elems_count - 12, elems_count, 1)
print(x)

plt.title('Month vs Passenger')
plt.ylabel('Total Passengers')
plt.grid(True)
plt.autoscale(axis='x', tight=True)
plt.plot(quote_close_values)
plt.plot(x, actual_predictions)
plt.show()

plt.title('Month vs Passenger')
plt.ylabel('Total Passengers')
plt.grid(True)
plt.autoscale(axis='x', tight=True)

plt.plot(quote_close_values[-train_window:])
plt.plot(x, actual_predictions)
plt.show()
