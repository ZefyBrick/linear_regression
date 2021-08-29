from reading_and_validation import read_validate_estimate


def main():

    theta_0, theta_1, km = read_validate_estimate()
    result = theta_0 + theta_1 * km
    print("theta_0  = " + str(theta_0) + "\ttheta_1 = " + str(theta_1))
    print('Стоимость авто при пробеге ' + str(km) + ' км равна ' + str(result))


if __name__ == '__main__':
    main()
