import matplotlib.pyplot as plt


def exibir(matriz: list[list[int]], pos_x: int | None = None, pos_y: int | None = None) -> None:
    plt.imshow(matriz, cmap="gray")
    plt.nipy_spectral()

    if pos_x is not None and pos_y is not None:
        plt.plot([pos_y], [pos_x], marker="o", color="r", ls="")

    plt.show()
