import numpy as np

def step_function(x):
    """
    入力xに対し、0 <= x の時は 0, x > 0 の時は1を返却する
    ステップ関数
    
    Parameters
    ----------
    x: numpy.ndarray
        入力xの配列
    """
    y = x > 0
    return y.astype(np.int)

def sigmoid(x):
    """
    シグモイド関数
    
    Parameters
    ----------
    x: numpy.ndarray
        入力xの配列
    """
    return 1 / (1 + np.exp(-x))

def relu(x):
    """
    入力xに対し、x > 0 の時は x, x <= 0 の時は0を返却する
    ReLU関数
    
    Parameters
    ----------
    x: numpy.ndarray
        入力xの配列
    """
    return np.maximum(0, x)