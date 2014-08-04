# 3D Viewer edX XBlock #
This XBlock allows students to upload .obj 3D models and use them as part of a course.
You can easily integrate the XBlock into Open edX platform.

## Installation instructions ##
In order to install the XBlock into your Open edX devstack Server you need to:

  1. Download the XBlock from github. Place the files inside your server.
  2. Install your block:
        You must replace `/path/to/your/block` with the path where you have downloaded the XBlock

        $ vagrant ssh
        vagrant@precise64:~$ sudo -u edxapp /edx/bin/pip.edxapp install /path/to/your/block

  3. Enable the block:

        #.  In ``edx-platform/lms/envs/common.py``, uncomment::

            # from xmodule.x_module import prefer_xmodules
            # XBLOCK_SELECT_FUNCTION = prefer_xmodules

        #.  In ``edx-platform/cms/envs/common.py``, uncomment::

            # from xmodule.x_module import prefer_xmodules
            # XBLOCK_SELECT_FUNCTION = prefer_xmodules

        #.  In ``edx-platform/cms/envs/common.py``, change::

            'ALLOW_ALL_ADVANCED_COMPONENTS': False,

            to::

            'ALLOW_ALL_ADVANCED_COMPONENTS': True

  4. Add the block to your courses' advanced settings in Studio:


        #. Log in to Studio, and open your course
        #. Settings -> Advanced Settings
        #. Change the value for the key ``"advanced_modules"`` to ``mt3d``


## Using the XBlock in the course ##
In the Studio go to:

![Settings->Advanced Settings](https://raw.githubusercontent.com/ExtensionEngine/xblock_3d_viewer/master/doc/img/1.png)

Add a mt3d policy key on the advanced_modules keys

![Policy key added](https://raw.githubusercontent.com/ExtensionEngine/xblock_3d_viewer/master/doc/img/2.png)

After that, a new button called Advanced will appear in your unit edit view

![Advanced](https://raw.githubusercontent.com/ExtensionEngine/xblock_3d_viewer/master/doc/img/3.png)

Add a new option called mt3d, which will add the component with the default 3D Viewer to the course.

![Adding 3D Viewer](https://raw.githubusercontent.com/ExtensionEngine/xblock_3d_viewer/master/doc/img/4.png)

You can change the parameters of the 3D Viewer by pressing the edit button.

![Display 3D Viewer](https://raw.githubusercontent.com/ExtensionEngine/xblock_3d_viewer/master/doc/img/5.png)

Right now you can change:

    1. Title of the XBlock
    2. Location of the 3D model
    3. Top and bottom background color
    4. Width and height of the 3D Viewer

![Editing 3D Viewer](https://raw.githubusercontent.com/ExtensionEngine/xblock_3d_viewer/master/doc/img/6.png)

## Student interaction with the XBlock: ##

    1. Zooming in and out of the 3D model
    2. Rotating the 3D model up, down, left and right
