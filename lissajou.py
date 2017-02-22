import numpy as np
import matplotlib.pyplot as plt

def car_sig(car, sig, rng, phi):
    return [car.calculate(angle, phi) * sig.calculate(angle, phi) for angle in rng]

class Wave:
    def __init__(self, amplitude = 1, frequency = 1):
        self.amplitude = amplitude
        self.frequency = frequency
        
    def calculate(self, angle, phi, deg=True):
        if deg:        
            return self.amplitude * np.sin(self.frequency
            * angle * np.pi/180 + phi)
        else:
            return self.amplitude * np.sin(self.frequency
            * angle + phi)
            
class LissCurve:        
    def __init__(self, carx = Wave(), sigx = Wave(), cary = Wave(), sigy = Wave(), val = np.linspace(0,4000,2000)):
        self.carx = carx
        self.sigx = sigx
        self.cary = cary
        self.sigy = sigy
        self.wavex = car_sig(carx, sigx, val, phi=0)
        self.wavey = car_sig(cary, sigy, val, phi=0)
        self.name = ('Lissajou_{cfx}-{sfx}-{cfy}-{sfy}.png'
                    .format(cfx=self.carx.frequency,
                            sfx=self.sigx.frequency,
                            cfy=self.cary.frequency,
                            sfy=self.sigy.frequency))
        
    def plot_lissajou(self):
        fig = plt.figure(facecolor='w', figsize = (5,5), dpi=300)
        plt.plot(self.wavex,self.wavey, c='k')
        plt.xlim([-1.05,1.05])
        plt.ylim([-1.05,1.05])
        plt.gca().axis('off')
        plt.savefig(self.name)
        plt.close()
        
plt.ioff()
np.random.seed(1234)
for i in range(200):
    res = 1
    params = np.random.randint(1,21, size = 4)
    
    carx = Wave(frequency = params[0]*res)
    sigx = Wave(frequency = params[1]*res)
    
    cary = Wave(frequency = params[2]*res)
    sigy = Wave(frequency = params[3]*res)
    
    keys = ['carx', 'sigx', 'cary','sigy']
    items = [carx, sigx, cary, sigy]
    args = dict(zip(keys, items))
    
    l = LissCurve(**args)
    l.plot_lissajou()
    
    print(l.name)
