<?php
$html = file_get_contents('c:/xampp/htdocs/luci/scratch/tsa.html');
$pos = strpos($html, 'id="cta-banner"');
if ($pos === false) {
    $pos = strpos($html, 'cta-banner');
}
while ($pos !== false) {
    echo "Found at $pos:\n";
    echo substr($html, $pos, 1500) . "\n===================================\n";
    $pos = strpos($html, 'cta-banner', $pos + 1000);
}

