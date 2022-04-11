# recommender_system

To customize the config file and make it point at the correct file in your filesystem, add the following line to (hidden folder) `.git/info/exclude` :

```
config.cnf
```

And then run the following command:

```
git update-index --assume-unchanged config.cnf
```
