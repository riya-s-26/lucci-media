<?php
$html = file_get_contents('c:/xampp/htdocs/luci/scratch/tsa.html');
preg_match_all('/(?:Our city|Midtown|creative asset|dynami[ck])/i', $html, $matches, PREG_OFFSET_CAPTURE);
echo "Matches in tsa.html (homepage): " . count($matches[0]) . "\n";
foreach ($matches[0] as $m) {
    echo "Found at offset {$m[1]}: " . $m[0] . "\n";
    echo substr($html, max(0, $m[1] - 300), 800) . "\n-------------------\n";
}

