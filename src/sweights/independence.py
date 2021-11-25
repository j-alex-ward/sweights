import numpy as np
from scipy.stats import kendalltau

def kendall_tau(x,y):
    assert(len(x)==len(y))
    err_approx = 1./np.sqrt(len(x))
    return ( kendalltau(x,y).correlation, err_approx, kendalltau(x,y).pvalue )

    raise RuntimeWarning('This function is depreciated use scipy.stats.kendalltau instead')
    factor = 2./(len(x)*(len(x)-1))
    su = 0.
    for i in range(len(x)):
        for j in range(i,len(x)):
            su += np.sign(x[i]-x[j])*np.sign(y[i]-y[j])

    return (factor*su, err_approx)

def plot(x,y,save=None,show=False):
    try:
      import matplotlib.pyplot as plt
      import uncertainties as u
    except:
      raise RuntimeError('matplotlib and uncertainties packages must be installed to plot independence \npip install matplotlib \npip install uncertainties')

    fig, ax = plt.subplots()
    ax.scatter(x,y)
    tau, err = kendall_tau(x,y)
    ax.text(0.7,0.9, r'$\tau = '+str(u.ufloat(tau,err)).replace('+/-',r'\pm')+'$', transform=ax.transAxes, backgroundcolor='w')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    fig.tight_layout()
    if save: fig.savefig(save)
    if show: plt.show()
    return fig, ax

if __name__=="__main__":

    a = list(range(10))
    b = list(reversed(range(10)))
    #plot(a,b)

    x = np.random.uniform(size=1000)
    y = np.random.uniform(size=1000)
    plot(x,y)
