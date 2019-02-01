import logRegres

if __name__ == '__main__':
    data_mat, label_mat = logRegres.load_dataset()

    result = logRegres.grad_ascent(data_mat, label_mat)
    print(result)

    result = logRegres.plot_best_fit(result)
