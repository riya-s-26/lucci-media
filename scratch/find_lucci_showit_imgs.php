<?php
$html = file_get_contents('c:/xampp/htdocs/luci/scratch/luccimedia.html');
preg_match_all('/(?:static\.showit\.co[^\s"\'\)]+|[a-zA-Z0-9_-]+\/[0-9]+\/[a-zA-Z0-9_\-\.]+\.(?:jpg|jpeg|png|webp))/i', $html, $matches);
$imgs = array_unique($matches[0]);
echo "Showit matches: " . count($imgs) . "\n";
foreach (array_slice($imgs, 0, 50) as $img) {
    if (strpos($img, 'http') === false) {
        $img = 'https://static.showit.co/1200/' . $img;
    }
    echo $img . "\n";
}

