# Ball in 2D Well simulation

In this simulation, a ball is rolling in a well following a certain continuous function 
<a href="http://www.codecogs.com/eqnedit.php?latex=f&space;\in&space;C^1(\mathbb{R})" target="_blank"><img src="http://latex.codecogs.com/gif.latex?f&space;\in&space;C^1(\mathbb{R})" title="f \in C^1(\mathbb{R})" /></a>

The simulation is based on the principle of Energy conservation. 

<a href="http://www.codecogs.com/eqnedit.php?latex=E=mgy(x)&plus;\frac{1}{2}mv^2" target="_blank"><img src="http://latex.codecogs.com/gif.latex?E=mgy(x)&plus;\frac{1}{2}mv^2" title="E=mgy(x)+\frac{1}{2}mv^2" /></a>
 
This equation give the speed magnitude for a given x position. To obtain the speed orientation, the following equation is used:

<a href="http://www.codecogs.com/eqnedit.php?latex=\theta=\text{atan}(f'(x))" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\theta=atan(f'(x))" title="\theta=\atan(f'(x))" /></a>

With these two information about speed, the speed vector can be constructed and used to find the next position using the temporal finite difference equation:

<a href="http://www.codecogs.com/eqnedit.php?latex=\vec{x}_{i&plus;1}=\vec{x}_i&plus;\vec{v}_i&space;\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\vec{x}_{i&plus;1}=\vec{x}_i&plus;\vec{v}_i&space;\Delta&space;t" title="\vec{x}_{i+1}=\vec{x}_i+\vec{v}_i \Delta t" /></a>

When the ball reaches the highest point of its position, the kinetic energy becomes null and therefore the algorithm must manually move the
particle in the opposite direction to restart the movement.


# Functions
Any differentiable function can be used to generate a well.

# Save gifs
To make a gif, you must use the savefig parameter when calling the code.

``` 
python3 2D_Puit.py savefig
```

The pictures will be stored in the picture2D folder. Than you can use a software tool to make gifs.

I personally use imagemagick

```
sudo apt-get install imagemagick
cd pictures2D
convert delay -2 -loop 0 `ls -v *.jpg` my_animation.gif 
```

![Alt Text](../../images/finite_diff/animation_puit2D.gif)
