import numpy as np


def softmax(x):
    """Compute the softmax function for each row of the input x.
    Arguments:
    x -- A N dimensional vector or M x N dimensional numpy matrix.

    Return:
    x -- You are allowed to modify x in-place
    """
    orig_shape = x.shape

    if len(x.shape) > 1:
        #Matrix
        maxVec=np.max(x,axis=1)
        maxVec=np.reshape(maxVec,(maxVec.size,-1))
        expX=np.exp(x-maxVec)
        sumVec=np.sum(expX,axis=1)
        sumVec=np.reshape(sumVec,(sumVec.size,-1))
        s=expX/sumVec
    else:
        # Vector
        maxVal=np.max(x,axis=0)
        expX=np.exp(x-maxVal)
        sumVal=np.sum(expX,axis=0)
        s=expX/sumVal

    assert s.shape == orig_shape
    return s


def test_softmax_basic():
    """
    Some simple tests to get you started.
    Warning: these are not exhaustive.
    """
    print "Running basic tests..."
    test1 = softmax(np.array([1,2]))
    print test1
    ans1 = np.array([0.26894142,  0.73105858])
    assert np.allclose(test1, ans1, rtol=1e-05, atol=1e-06)

    test2 = softmax(np.array([[1001,1002],[3,4]]))
    print test2
    ans2 = np.array([
        [0.26894142, 0.73105858],
        [0.26894142, 0.73105858]])
    assert np.allclose(test2, ans2, rtol=1e-05, atol=1e-06)

    test3 = softmax(np.array([[-1001,-1002]]))
    print test3
    ans3 = np.array([0.73105858, 0.26894142])
    assert np.allclose(test3, ans3, rtol=1e-05, atol=1e-06)

    print "You should be able to verify these results by hand!\n"


def test_softmax():
    """
    Use this space to test your softmax implementation by running:
        python q1_softmax.py
    This function will not be called by the autograder, nor will
    your tests be graded.
    """
    print "Running your tests..."
    ### YOUR CODE HERE
    raise NotImplementedError
    ### END YOUR CODE


if __name__ == "__main__":
    test_softmax_basic()
    test_softmax()
