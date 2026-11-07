<?php
$html = file_get_contents('c:/xampp/htdocs/luci/scratch/tsa.html');
$pos = strpos($html, 'cta-banner');
if ($pos !== false) {
    echo substr($html, $pos - 100, 3500);
} else {
    echo "not found";
}

