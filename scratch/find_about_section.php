<?php
$html = file_get_contents('c:/xampp/htdocs/luci/scratch/tsa_about.html');
preg_match_all('/"slug":"([^"]+)"/i', $html, $slugs);
echo "Slugs: " . implode(', ', array_unique($slugs[1])) . "\n";

// Search for any text containing Manhattan or NYC or city
preg_match_all('/(?:Manhattan|NYC|creative asset|Midtown|city)/i', $html, $matches, PREG_OFFSET_CAPTURE);
echo "Found " . count($matches[0]) . " keyword matches.\n";
foreach (array_slice($matches[0], 0, 5) as $m) {
    echo "Offset: {$m[1]} - " . substr($html, max(0, $m[1] - 100), 400) . "\n-------------------\n";
}

