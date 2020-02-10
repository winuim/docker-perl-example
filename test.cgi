#!/usr/local/bin/perl
use Log::Minimal;

print "Content-type: text/html\n\n";
print "Hello CGI\n";

$ENV{LM_DEBUG} = 1;

critf("%s","foo"); # 2010-10-20T00:25:17 [CRITICAL] foo at example.pl line 12
warnf("%d %s %s", 1, "foo", $uri);
infof('foo');
debugf("foo");
 
# with full stack trace
critff("%s","foo");
# 2010-10-20T00:25:17 [CRITICAL] foo at lib/Example.pm line 10, example.pl line 12
warnff("%d %s %s", 1, "foo", $uri);
infoff('foo');
debugff("foo");

my $serialize = ddf({ 'key' => 'value' });

# die with formatted message
# croakf('foo');
# croakff('%s %s', $code, $message);

local $Log::Minimal::AUTODUMP = 1;
 
critf({ foo => 'bar' });
critf("dump is %s", { foo => 'bar' });
