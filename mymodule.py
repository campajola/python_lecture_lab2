def fit_lineare_pesato(x,y,w) :
    """
    questa funzione calcola i parametri della retta di best fit y = a + b*x 
    usando le formule dei minimi quadrati pesati.
    N.B. w è il vettore dei pesi, dove il peso w_i è l'inverso del quadrato dell'incertezza 
    sulla coordinata y_i dell'i-esimo punto.    
    """
    W = np.sum(w)
    S_x = np.sum(x*w)     
    S_xx = np.sum(x*x*w)     
    S_y = np.sum(y*w)
    S_xy = np.sum(x*y*w)
    D = W * S_xx - S_x**2
    A = (S_xx * S_y - S_x * S_xy) / D
    B = (W * S_xy - S_x * S_y) / D
    cov_00 = S_xx / D
    cov_11 = W / D
    cov_01 = -S_x / D
    # Compute chi^2 = \sum w_i (y_i - (a + b * x_i))^2
    chi2 = np.sum (w * (y-(a+b*x))**2)
    return a,b,cov_00,cov_11,cov_01,chi2

