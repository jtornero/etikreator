Etikreator
==========

(c) 2015 Jorge Tornero Núñez, http://imasdemase.com @imasdemase

Etikreator is just a small application programmed in Python/Pyqt4 to produce labels for otolith storing slides with a Zebra Technologies label printer or any ZPL2 compatible printer, providing it is compatible with 38x13 (1.5"x0.5") labels.

The software has been tested with a Zebra GK420t printer with ethernet connection. Despite of this, adaptation of the software to other printers is just matter of tweaking the code a little, particulary ZPL2 code inside the methods related to label creation.

The slides I use can be considered standard in the institution i work for (Spanish Institute of Oceanography) for storing anchovy and sardine otoliths. In Spain these slides are manufactured by Hedican (www.hedican.com).

Because we use Eukitt mounting medium to fix the otoliths to the slide and also otolith slides are supposed to be stored for yeqars, I've chosen Z-Ultimate 3000T White Desk labels in combination with ribbon 5095. Of course, you can choose whatever label/ribbon you want to use depending on your particular application.

Usage
=====

I usually make two kinds of labels. One sort for labelling slides for otoliths coming from fish market samples and another for otoliths coming from survey samples, thus the two tabs in the tab widget.

In any case, the comboboxes are editable so, despite the hard-coded values of the combo (which could be changed thorug QtDesigner), you could provide whatever value you want.

Just fill the data for the labels and press print to get your labels printed.

Notice that the software includes a sentence in ZPL2 language which sets an alias for some fonts. In case you don't have installed that font in your printer, you should modify the source to get a nice print.

Changelog
=========

10/07/2015 First working version
18/07/2015 Support for labeling vials/single samples (it means one label, one number)
21/07/2015 Added a button for media calibration

Further improvements
====================

- Get comboboxes values from a configuration file at startup
- GUI translation
- Better font management
- Variable sample number in slides. Actually fixed to 10 as it is the standard for otolith slides.

License
=======
Etikreator is released under GPL V3.0 license. For further information please see http://www.gnu.org/licenses/gpl-3.0.html
