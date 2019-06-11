# Collection of scripts to make simple plots in r using ggplot

## Input data

An excel spreadsheet (preferebly in csv format) is the standard input file for plotting using ggplot.

Eg. A table named `animal_species_count.csv` with animal phyla and the number of species in each.

| Clade_name       | Species_count |
| ---------------- | ------------- |
| Porifera         | 	1	   |
| Ctenophora       |	3	   |
| Cnidaria         |	6	   |
| Lophotrochozoa   |	11	   |
| Ecdysozoa        |	15	   |
| Deuterostomia    |	33	   |

You can load the data file in manually into R or import it from ((R commmand line)[https://www.statmethods.net/inputimportingdata.html])

```Shell
df <- read.table("Filename.csv", header = TRUE)
```

## Using ggplot to create plots of the data

In order to create plots using ggplot you first need to make sure the package is installed in r by typing 

```Shell
install.packages("ggplot2")
```

Then load the package by typing 
```Shell
library(ggplot2)
```

There are two main components of any ggplot plot.

* First is `ggplot(animal_species_count, aes(x = Clade_name, y = Species_count))`, with clade names on the x axis and species counts on the y axis

* Second is the type of plot you wish to make (in this case a barchart `geom_bar(stat = "identity", fill = "blue")`

**Note** `geom_bar` can be changed to any type of plot eg. scatter plot: `geom_point`, box plot: `geom_boxplot` or violin plot: `geom_violin` etc.

Together these two main components can be written as:

```Shell
ggplot(taxa_spread, aes(x = Clade_name, y = Species_count)) + 
geom_bar(stat = "identity", fill = "blue")
```

To retain the order of the rows from the input data file you must change the axis values to:

```Shell
ggplot(taxa_spread, aes(x = factor(Clade_name, levels=unique(Clade_name)), y = Species_count)) +
geom_bar(stat = "identity", fill = "blue")
```

![Example plot 1.](first_plot.png)


### Additional parameters to make it look nicer

Once we have this bar chart we can add some additional pieces of information to the code to make the final image look a bit nicer.

1. **Add your own colours to the bars**

Change your `geom_bar(fill="blue")` variable to `aes(fill=Clade_name)` to match each x axis value.

Then add an additional line using `scale_fill_manual()` to provide your own colours (6 animal phyla means I must provide 6 colours)

```Shell
ggplot(taxa_spread, aes(x = factor(Clade_name, levels=unique(Clade_name)), y = Species_count)) +
geom_bar(stat = "identity", aes(fill=Clade_name)) + 
scale_fill_manual(values = c("#f0027f", "#7fc97f", "#fb8072", "#fdc086", "#ffff99", "#386cb0"))
```

![Example plot 2.](second_plot.png)

**Tip** Hex colours can be obtained from the useful website ((colorbrewer.org)[http://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3])

---

2. **Remove background colour and unecessary space**

To get a blank white background add `theme_classic()`

To remove space between the axis and the bars use `scale_y_continuous()`

```Shell
ggplot(taxa_spread, aes(x = factor(Clade_name, levels=unique(Clade_name)), y = Species_count)) +
geom_bar(stat = "identity", aes(fill=Clade_name)) + 
scale_fill_manual(values = c("#f0027f", "#7fc97f", "#fb8072", "#fdc086", "#ffff99", "#386cb0")) +
theme_classic() +
scale_y_continuous(expand = c(0,0,0.1,0))
```

![Example plot 3.](third_plot.png)

---

3. **Change the axis label names**

Add `labs(x = "", y = "")` to change the name of your x and y axis (insert NULL if you do not want an axis label)

```Shell
ggplot(taxa_spread, aes(x = factor(Clade_name, levels=unique(Clade_name)), y = Species_count)) +
geom_bar(stat = "identity", aes(fill=Clade_name)) +
scale_fill_manual(values = c("#f0027f", "#7fc97f", "#fb8072", "#fdc086", "#ffff99", "#386cb0")) +
theme_classic() +
scale_y_continuous(expand = c(0,0,0.1,0)) +
labs(x = "Clade names", y = "Species count")
```

4. **Add in or edit text within the plot**

* To add additional text or change the size, position or orientation of the text within the plot use `theme()`

Remove x axis labels: `theme(axis.text.x = element_blank())`
Increase size of x axis title `theme(axis.title.x = element_text(size = 20))`
Remove tick marks on x axis bar `theme(axis.ticks.x = element_blank())`
Increase size of legend text `theme(legend.text=element_text(size=12))`


* Add in values above the bars using `geom_text()` and the y axis values

`geom_text(aes(label = paste0(Species_count)), vjust = -1, size = 3, color = "black")`

```Shell
ggplot(taxa_spread, aes(x = factor(Clade_name, levels=unique(Clade_name)), y = Species_count)) +
geom_bar(stat = "identity", aes(fill=Clade_name)) + 
scale_fill_manual(values = c("#f0027f", "#7fc97f", "#fb8072", "#fdc086", "#ffff99", "#386cb0")) +
theme_classic() +
scale_y_continuous(expand = c(0,0,0.1,0)) +
labs(x = "Clade names", y = "Species count") +
theme(axis.text.x = element_blank(), axis.title.x = element_text(size = 20), axis.title.y = element_text(size = 20), axis.text.y = element_text(size = 15), axis.ticks.x = element_blank(), legend.text=element_text(size=12)) +
geom_text(aes(label = paste0(Species_count)), vjust = -1, size = 6, color = "black")
```

![Example plot 4.](final_plot.png)

---

To save a plot called p as a png:

```Shell
png("plot_name.png")
print(p)
dev.off()
```

To save as a pdf use `pdf("plot_name.pdf")`