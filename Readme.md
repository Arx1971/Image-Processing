<h3>Image Processing</h3>
<ul>
    <li>
        Compute the histogram of Color Image. The
        script also has to plot the histograms of each band of the image separately (Read, Green, and
        Blue), as well as the gray level intensity image resulting of averaging the color bands. Use
        OpenCV, numpy, and Matplot to load, process, and visualize the information.
        <h3>Result: </h3>
        <h4>Over Exposed Result: </h4>
        <img src="https://github.com/Arx1971/Image-Processing/blob/master/Image-Histogram/overexposed_plot.png"
        alt="Over Exposed Plot"
        style="float: left; margin-right: 10px;" />
        <h4>Under Exposed Result: </h4>
        <img src="https://github.com/Arx1971/Image-Processing/blob/master/Image-Histogram/underexposed_plot.png"
        alt="Under Exposed Plot"
        style="float: left; margin-right: 10px;" />
    </li>
    <li>
        Capture an image with a uniform background, then put an object on the scene and get a second
        image of the scene. Create a program to process the previous two images; the script has to
        generate a binary image, where the pixels belonging to the object (foreground) take values of
        one and pixels from the background takes values of zero respectively. To do this, use the
        subtraction operator to obtain the difference between the first image and the second image,
        and then apply a thresholding process to generate the binary image.
        Test different values for the threshold until obtaining the best results. Quantify the number of
        pixels that belong to the object of interest. Visualize histograms and the binary image
        <img src="https://github.com/Arx1971/Image-Processing/blob/master/Image-Histogram/binary_image.png"
        alt="Under Exposed Plot"
        style="float: left; margin-right: 10px;" />
    </li>
    
</ul>