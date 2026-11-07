<?php
$html = file_get_contents('c:/xampp/htdocs/luci/scratch/tsa.html');
$pos = strpos($html, 'id="nyc-section"');
if ($pos !== false) {
    echo substr($html, $pos, 8000);
} else {
    echo "not found";
}

