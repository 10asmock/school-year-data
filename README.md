# school-year-data
A Python project which parses JSON data from the college scorecard API and displays them on a web page.

## HOW TO USE

- Install [Virtual Box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) and [Vagrant](https://www.vagrantup.com/downloads.html)

- Download this repository into any computer directory.

- From your terminal, inside the ```vagrant``` subdirectory, run the command ```vagrant up```. This will cause Vagrant to download the Linux operating system and install it.

- When vagrant up is finished running, you will get your shell prompt back. At this point, you can run ```vagrant ssh``` to log in.

- In the VM, type in ```cd /vagrant``` to access the files containing school-year-data.

- Once inside, type in ```cd /scripts``` and run the command ```python test.py``` to transfer JSON data from the college scorecard API to index.html.

- Click on ```index.html``` to see all JSON data stored in HTML file.

- ADDENDUM: Alternatively, due to a bug (recently fixed) in ```test.py```, click on ```index.html``` to view dynamic web page consisting of charts and graphs of JSON data manually parsed into HTML document. Do not run ```test.py``` beforehand.

