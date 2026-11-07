<?php
$html = file_get_contents('c:/xampp/htdocs/luci/scratch/luccimedia.html');
// Extract all text inside HTML tags
$clean = strip_tags($html);
$lines = explode("\n", $clean);
$meaningful = [];
foreach ($lines as $line) {
    $t = trim($line);
    if (strlen($t) > 10 && strlen($t) < 150) {
        $meaningful[] = $t;
    }
}
$meaningful = array_unique($meaningful);
file_put_contents('scratch/lucci_copy.txt', implode("\n", $meaningful));
echo "Extracted " . count($meaningful) . " copy lines.\n";
foreach (array_slice($meaningful, 0, 40) as $c) {
    echo $c . "\n";
}

