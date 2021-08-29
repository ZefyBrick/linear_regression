from sys import exit
from reading_and_validation import read_validate_train
import graph
import csv


def main():

    accur, learning_rate, x_tr, y, vis, error = read_validate_train()
    theta_0, theta_1, sum_y = 0.0, 0.0, sum(y)
    m = len(y)
    mx = max(x_tr)
    x = [i / mx for i in x_tr]
    n_iter, error_por = 0, [1]
    while 1 - error_por[n_iter] < accur:
        errors, error_i = [0.0, 0.0], 0
        for j in range(m):
            predict = theta_0 + theta_1 * x[j]
            errors[0] += predict - y[j]
            errors[1] += (predict - y[j]) * x[j]
            error_i += abs(predict - y[j])
        try:
            theta_0 = theta_0 - learning_rate / m * errors[0]
            theta_1 = theta_1 - learning_rate / m * errors[1]
        except OverflowError as over:
            print('Слишком большие значения входных показателей!')
            exit()
        error_por.append(error_i / sum_y)
        n_iter += 1
        if n_iter > 2000000:
            print('Измените значения параметров для обучения модели!')
            exit()
    print("Модель обучилась за " + str(n_iter) + " итераций")
    theta_1 = theta_1 / mx
    print("theta_0  = " + str(theta_0) + "\ttheta_1 = " + str(theta_1))
    with open('results.csv', 'w') as csv_file:
        file_writer = csv.writer(csv_file, delimiter=',',
                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow([theta_0, theta_1])
    if vis:
        graph.get_plot(x_tr, y, theta_0, theta_1)
    if error:
        graph.get_plot_error(n_iter, error_por)


if __name__ == '__main__':
    main()
