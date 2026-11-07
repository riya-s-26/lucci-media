<?php
$html = file_get_contents('c:/xampp/htdocs/luci/scratch/tsa.html');
// Find CSS for cta-banner
preg_match_all('/\.si[eb]-cta-banner[^{]*\{[^}]*\}/s', $html, $matches);
foreach ($matches[0] as $m) {
    echo $m . "\n";
}

