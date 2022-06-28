# Unlocking Environmental Narratives - Chapter 7

### Code

Python scripts for pre-processing the Loch Lomond data. The original files are too long to process comfortably with some NLP tools, so each book can be automatically segmented into sections.

`split-western.py` is for the files of type Project Gutenberg which are in HTML. Each document represents a chapter in the book (according to the H2 HTML tag).

`split-other.py` is for the plain text files which have been OCR-ed. These require special processing to first split into sentences, and to remove some extra blank lines which otherwise cause problems for linguistic processing. This is to ensure that when the book is split into sections, a section does not cross a sentence boundary.

### Collection Methodology:
- The sample corpus was selected from archive.org using a date-limited search (earliest) of 'Loch Lomond' (text sources only), with a range intended to include different authors and as many guidebooks as possible. The following criteria were thus applied:
- only text sources were selected (as other source types cannot be processed automatically using our methodology)
- the 'first' publication date versions of each guidebook were selected; 
- a date cut-off of 1895 was applied to limit sample size; 
The corpus was then compared to British Library holdings and Wikipedia in order to check for any key texts to add to the sample.

### Document List:                                                                                                                                                          
1) Journey to the Western Isles, Johnson and Boswell, 1785. https://www.gutenberg.org/files/2064/2064-h/2064-h.htm;  https://www.gutenberg.org/files/2064/2064-h/2064-h.htm#startoftext
2) The picture of Glasgow, and strangers' guide; with a sketch of a tour to Loch-Lomond, R Chapman (1818) https://archive.org/details/pictureofglasgow00unse/page/n9
3) The steam boat companion; and stranger's guide to the Western islands and Highlands of Scotland (1820), https://archive.org/details/bub_gb_x5sHAAAAQAAJ/page/n4
4) Guide to the romantic scenery of Loch-Lomond, Loch-Ketturin, the Trosachs, &c, James Lumsden, (1831) https://archive.org/details/guidetoromantic00songoog/page/n5
5) Black’s Guide to the Trossachs (1853), https://archive.org/details/blacksshillinggu00ediniala/page/n4
6) Nelson’s Tourist Guide (1858), https://archive.org/details/nelsonstouristsg00thom/page/n2
7) Edinburgh & Glasgow to Stirling: Doune, Callander, Lake of Menteith, Loch Ard, Loch Achray, the Trosachs, Loch Katrine, Loch Lomond, Keddie and Gray (1873), https://archive.org/details/edinburghglasgowkedd/page/n13
8) Shearer's Guide to Stirling, Dunblane, Callender, the Trossachs and Loch Lomond, Shearer (1895), https://archive.org/details/shearersguidetos00shea/page/2

### Format:

The documents were collected as html files since these contain useful formatting information for automatic processing. Plain text versions can also be made available if required.
Limitations:  non-digitised work (at British Library: Guide to Loch Lomond, Richardson, 1798; Baird's Guide, 1853, Brydone's Guide, 1856; Tourist Picturesque Guide, 1873; Shaw's Picturesque, 1878).

### Note:

In this directory are several folders.
Html contains the original html files
Split.zip is a zip file of the cleaned versions, segmented into sections per book, as described in the documentation. Python scripts for doing the splitting are also included in the code directory.
loch-lomond-all-datastore.zip s a zip file containing a Lucene datastore (viewable in GATE) with the entire corpus processed by the GATE Geo application, including the latest Loch Lomond geographical terms. This can be used for searching the corpus (for anyone with basic GATE skills).

