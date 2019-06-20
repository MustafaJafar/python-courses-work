%refrence : https://www.mathworks.com/videos/color-based-segmentation-with-live-image-acquisition-68771.html

%Get the image 
%Im = imread('images/candy1.jpg');
Im = imread('images/candy2.PNG');
%Im = imread('images/candy3.jpg');
imshow(Im);

%-----------------------

%Threshold the image on each color plane 
Im = im2double(Im); 
[height,width, color_planes] = size(Im); 

%Extract individuals plane from RGB image 
imR = squeeze (Im(:,:,1));
imG = squeeze (Im(:,:,2));
imB = squeeze (Im(:,:,3));

%Thresholding on individual planes 
imBinaryR = im2bw(imR , graythresh(imR));
imBinaryG = im2bw(imG , graythresh(imG));
imBinaryB = im2bw(imB , graythresh(imB));
imBinary = imcomplement(imBinaryR&imBinaryG&imBinaryB);

imshow(imBinary);

%---------------

%Morphological opening
se = strel('disk',7);
imClean = imopen(imBinary , se) ;

%Fill holes and clear border 
imClean = imfill(imClean , 'holes');
imClean = imclearborder(imClean);
imshow(imClean);

%--------------

%Segmented gray-level image 
[labels,numLabels] = bwlabel(imClean);
disp(['Number of objects detected: ' num2str(numLabels)]);

%Initialize matrices 
rLabel = zeros(height,width);
gLabel = zeros(height,width);
bLabel = zeros(height,width);

%-------------

%Get average color vector for each labeld region 

for i = 1 : numLabels 
    rLabel(labels == i) = median(imR(labels == i));
    gLabel(labels == i) = median(imG(labels == i));
    bLabel(labels == i) = median(imB(labels == i));
end
imLabel = cat (3 , rLabel, gLabel , bLabel);
imshow(imLabel)

impixelinfo(gcf);

%---------------

%Get desired color to segment 
[x,y] = ginput(1);
selColor = imLabel(floor(y),floor(x),:);

%Convert to LAB color space 
C = makecform('srgb2lab');
imLAB = applycform(imLabel , C);
imSelLAB = applycform(selColor , C);

%Extract a* and b* values 
imA = imLAB(:,:,2);
imB = imLAB(:,:,3);
imSelA = imSelLAB(1,2); %extract a*
imSelB = imSelLAB(1,3); %extract b*

%Compute distance from selected color
distThresh = 20 ; 
imMask = zeros(height,width);
imDist = hypot(imA-imSelA , imB-imSelB);
imMask (imDist < distThresh) = 1 ;
[CLabel , cNum] = bwlabel(imMask);
imSeg = repmat(selColor , [height , width ,1]).*repmat(imMask , [1,1,3]);
imshow(imSeg);

%Plot the color segmented image 
figure,subplot(2,1,1), imshow(Im);
title(['Total number of objects = ' , num2str(numLabels)]);
subplot(2,1,2),imshow(imSeg);
title(['Number of objects of the selected color = ' num2str(cNum)]);
