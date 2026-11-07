<?php
$opts = [
    'http' => [
        'method' => 'GET',
        'header' => "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\r\n"
    ]
];
$context = stream_context_create($opts);
$html = @file_get_contents('https://thesocialagency.dk/', false, $context);
if (!$html) {
    echo "Failed to fetch\n";
    exit;
}
file_put_contents('scratch/tsa.html', $html);
echo "Length: " . strlen($html) . "\n";
preg_match_all('/(?:CUSTOM CONTENT|STRUCTURED EXECUTION|IMPACTFUL RESULTS|OUR STUDIO|CLIENT ARCHIVE)/i', $html, $matches, PREG_OFFSET_CAPTURE);
foreach ($matches[0] as $m) {
    $offset = $m[1];
    echo "Match: " . $m[0] . "\n";
    echo substr($html, max(0, $offset - 250), 600) . "\n------------------------\n";
}

