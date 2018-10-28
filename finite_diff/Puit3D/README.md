# Ball in 3D Well simulation

In this simulation, a ball is rolling in a well following a certain continuous function 
<a href="http://www.codecogs.com/eqnedit.php?latex=f&space;\in&space;C^1(\mathbb{R}^2)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?f&space;\in&space;C^1(\mathbb{R}^2)" title="f \in C^1(\mathbb{R})" /></a>

The simulation is based on the principle of the first Law of Newton

<a href="http://www.codecogs.com/eqnedit.php?latex=\sum\Vec{F}=&space;mg\hat{y}&plus;N&space;\hat{n}&space;=&space;m&space;\frac{\delta^2&space;\Vec{r}}{\delta&space;t&space;^2}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\sum\Vec{F}=&space;mg\hat{y}&plus;N&space;\hat{n}&space;=&space;m&space;\frac{\delta^2&space;\Vec{r}}{\delta&space;t&space;^2}" title="\sum\Vec{F}= mg\hat{y}+N \hat{n} = m \frac{\delta^2 \Vec{r}}{\delta t ^2}" /></a>

The normal vector of the surface can be computed by uing a parametric surface

<a href="http://www.codecogs.com/eqnedit.php?latex=\Vec{r}=(x,&space;y,&space;z(x&space;,y)))" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\Vec{r}=(x,&space;y,&space;z(x&space;,y)))" title="\Vec{r}=(x, y, z(x ,y)))" /></a>
 
 Then calculating the non-normalized normal vector
 
<a href="http://www.codecogs.com/eqnedit.php?latex=\Vec{n}&space;=&space;\frac{\delta&space;\Vec{r}}{\delta&space;x}&space;\times&space;\frac{\delta&space;\Vec{r}}{\delta&space;y}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\Vec{n}&space;=&space;\frac{\delta&space;\Vec{r}}{\delta&space;x}&space;\times&space;\frac{\delta&space;\Vec{r}}{\delta&space;y}" title="\Vec{n} = \frac{\delta \Vec{r}}{\delta x} \times \frac{\delta \Vec{r}}{\delta y}" /></a>

And finally normalizing

<a href="http://www.codecogs.com/eqnedit.php?latex=\hat{n}=\frac{\Vec{n}}{||\Vec{n}||}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\hat{n}=\frac{\Vec{n}}{||\Vec{n}||}" title="\hat{n}=\frac{\Vec{n}}{||\Vec{n}||}" /></a>


The normal force N is computed like this

<a href="http://www.codecogs.com/eqnedit.php?latex=N&space;=&space;-mg&space;\hat{y}&space;\cdot&space;\hat{n}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?N&space;=&space;-mg&space;\hat{y}&space;\cdot&space;\hat{n}" title="N = -mg \hat{y} \cdot \hat{n}" /></a>




# Functions
Any diffenrentiable function can be used to generate a well so feel free to experiment with your own. The user must calculate the normal vector analytically.

# Save gifs
To make a gif, you must set the savefig boolean to True. The pictures will be stored in the picture2D repository. Than you can use a software tool to make gifs.
I use imagemagick
```
sudo apt-get install imagemagick
cd pictures3D
convert delay -2 -loop 0 `ls -v *.jpg` my_animation.gif 
```

Enjoy your animations ;)

![Alt Text](https://github.com/gablabc/Numerical_Physics/blob/master/finite_diff/Puit3D/pictures3D/animation2.gif)
![Alt Text](https://github.com/gablabc/Numerical_Physics/blob/master/finite_diff/Puit3D/pictures3D/flower_top.gif)
![Alt Text](https://github.com/gablabc/Numerical_Physics/blob/master/finite_diff/Puit3D/pictures3D/circle_angle.gif)
![Alt Text](https://github.com/gablabc/Numerical_Physics/blob/master/finite_diff/Puit3D/pictures3D/circle_top.gif)

