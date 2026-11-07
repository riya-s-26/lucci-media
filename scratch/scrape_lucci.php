<?php
$opts = ['http' => ['header' => "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\r\n"]];
$html = @file_get_contents('https://luccimedia.com/', false, stream_context_create($opts));
if (!$html) {
    echo "Failed to fetch luccimedia.com\n";
    exit;
}
file_put_contents('scratch/luccimedia.html', $html);
echo "Fetched luccimedia.com, length: " . strlen($html) . "\n";
preg_match_all('/https?:\/\/[^\s"\'\(\)]+\.(?:jpg|jpeg|png|webp)/i', $html, $imgs);
$unique = array_unique($imgs[0]);
echo "Found " . count($unique) . " images:\n";
foreach (array_slice($unique, 0, 40) as $img) {
    echo $img . "\n";
}

