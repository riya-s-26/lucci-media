<?php
$opts = ['http' => ['header' => "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\r\n"]];
$ctx = stream_context_create($opts);
$html = @file_get_contents('https://thesocialagency.dk/about', false, $ctx);
if (!$html) {
    echo "Failed to fetch about page\n";
    exit;
}
file_put_contents('scratch/tsa_about.html', $html);
echo "Fetched TSA about page, length: " . strlen($html) . "\n";
preg_match_all('/(?:Our city|Midtown Manhattan|dynami[ck]|NYC is one)/i', $html, $matches, PREG_OFFSET_CAPTURE);
foreach ($matches[0] as $m) {
    $offset = $m[1];
    echo "Match: " . $m[0] . "\n";
    echo substr($html, max(0, $offset - 400), 1000) . "\n====================================\n";
}

