See: [Powerline](https://github.com/Lokaltog/powerline)

Added:
* Undotree plugin
* Tagbar plugin

```
git clone git://github.com/baopham/powerline-config.git ~/.config/powerline
```

Then put this in your `.zshrc` or `.bashrc`:
```
export PYTHONPATH=$PYTHONPATH:$HOME/.config/powerline
```

Tmux
----

Screenshot (omitting IP segment):

![screenshot](http://cl.ly/image/2f2j1q37023q/Screen%20Shot%202014-10-04%20at%209.36.01%20PM.png)

Put this in your `.tmux.conf`:
```
source ~/.config/powerline/powerline/bindings/tmux/powerline.conf
```
