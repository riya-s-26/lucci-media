<?php
$html = file_get_contents('c:/xampp/htdocs/luci/scratch/tsa_about.html');
$pos = strpos($html, 'id="image-banner"');
if ($pos === false) {
    $pos = strpos($html, 'image-banner');
}
while ($pos !== false) {
    echo "Found image-banner at $pos:\n";
    echo substr($html, $pos, 2500) . "\n====================================\n";
    $pos = strpos($html, 'image-banner', $pos + 1500);
}

