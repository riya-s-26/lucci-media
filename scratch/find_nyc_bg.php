<?php
$html = file_get_contents('c:/xampp/htdocs/luci/scratch/tsa.html');
$pos = strpos($html, '"slug":"nyc-section"');
if ($pos !== false) {
    echo substr($html, $pos, 1500);
} else {
    echo "not found";
}

