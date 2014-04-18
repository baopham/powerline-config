See: [Powerline](https://github.com/Lokaltog/powerline)

Added:
* Undotree segment

```
git clone git://github.com/baopham/powerline-config.git ~/.config/powerline
```

Then put this in your `.zshrc` or `.bashrc`:
```
export PYTHONPATH=$PYTHONPATH:$HOME/.config/powerline
```

Tmux
----

Screenshot (omitting IP segment): http://cl.ly/image/411m2p2O2Q17

Put this in your `.tmux.conf`:
```
source ~/.config/powerline/powerline/bindings/tmux/powerline.conf
```
