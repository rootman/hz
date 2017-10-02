<?php

/**
 * @param $urls
 * @return array
 */
function processUrls($urls)
{
    return array_map(function ($url) {
        return str_replace('&amp;', '&', $url);
    }, $urls);
}

/**
 * @param $urls
 * @return array
 */
function filterDocumentUrls($urls)
{
    return array_filter($urls, function ($url) {
        return strpos($url, 'show_document') !== false;
    });
}

/**
 * @param $text
 * @return mixed
 */
function extractUrls($text)
{
    preg_match_all('|https?:\/\/(www\.)?[-a-zA-Z0-9@:;%._\+~#=]{2,500}\.[a-z]{2,6}\b([-a-zA-Z0-9@:;%_\+.~#?&//=]*)|', $text, $matches);
    return $matches[0];
}

/**
 * @param $date
 * @return bool|string
 */
function scrapeByDate($date)
{
    $url = 'https://www.bger.ch/ext/eurospider/live/de/php/aza/http/index_aza.php?date=%d&lang=de&mode=news';

    return file_get_contents(
        sprintf($url, date('Ymd', $date))
    );
}

$result = scrapeByDate(time());
$urls = extractUrls($result);
$relevant =
    processUrls(
        filterDocumentUrls(
            $urls
        )
    );

file_put_contents('urls.txt', implode("\n", $relevant));

