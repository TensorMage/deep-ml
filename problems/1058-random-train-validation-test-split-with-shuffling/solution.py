import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    n=len(data)

    rng=np.random.default_rng(seed)
    indices=rng.permutation(n)

    train_part=int(n*train_frac)
    validation_part=train_part+int(n*validation_frac)

    shuffled_data=data[indices]

    train=shuffled_data[:train_part]
    validation=shuffled_data[train_part:validation_part]
    test=shuffled_data[validation_part:]

    return [train,validation,test]
