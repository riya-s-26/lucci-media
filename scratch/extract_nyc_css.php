<?php
$html = file_get_contents('c:/xampp/htdocs/luci/scratch/tsa.html');
preg_match_all('/\.si[eb]-nyc-section[^{]*\{[^}]*\}/s', $html, $matches);
foreach ($matches[0] as $m) {
    echo $m . "\n";
}

