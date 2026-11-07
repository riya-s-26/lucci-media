<?php
$h = file_get_contents('scratch/tsa.html');
preg_match('/<div[^>]*data-bid="nyc-section"[^>]*>.*?<\/div>\s*<\/div>\s*<\/div>/s', $h, $m);
if ($m) {
    echo $m[0];
} else {
    // search for nyc in divs
    preg_match_all('/<div[^>]*id="[^"]*nyc[^"]*"[^>]*>/i', $h, $m2);
    print_r($m2[0]);
}
