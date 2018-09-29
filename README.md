# Jenkins_Scripts

Some scripts used with Jenkins CI.

__Get_Jenkins_Active_Plugins.py__

This script prints out a list of the currently installed and 'active' plugins. It does _not_ show any plugins that are installed as dependencies of those plugins. 

This in effect prints out the plugsins that you would see in Jenkins Plugin Manager that are 'Enabled' with the dark blue checkbox, but not the ones with the light blue checkbox.

Eg: Here we see three plugins, however the SDK plugin is a dependency and will be installed automatically when required by another plugin, so we don't need to explicitly list it out.

![JenkinsCI](https://i.imgur.com/6WUnP6M.png)


If we run out script it will output:
```
amazon-ecs
ec2
```
These are the 'shortnames' of the plugins that are listed above.

