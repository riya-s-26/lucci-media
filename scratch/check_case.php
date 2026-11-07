<?php
$h = file_get_contents('scratch/tsa.html');
preg_match_all('/<p[^>]*>(.*?)<\/p>/is', $h, $m);
foreach (array_slice($m[1], 0, 10) as $t) {
    echo trim(strip_tags($t)) . "\n---\n";
}

