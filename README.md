# python-declarative-2to3

A cherry-pick of committed 2to3 code:

115 changed files
199 additions
214 deletions

https://github.com/CenterForOpenScience/osf.io/commit/1d11c3b11ea3b2dc2fa2797bdf779ae05b8c87ea

The `./test-equal-*` scripts are the ones that matter.

Samples for `test-equal-*`:

```
rvt:python-declarative-2to3/ (master*) $ ./test-equal-next.sh                                                          [21:41:15]

real    0m2.053s
user    0m15.104s
sys     0m0.580s
{
  "number_of_files": 115,
  "lines_of_code": 55648,
  "number_of_matches": 11,
  "total_time": 899.7080326080322
}Diffs
rvt:python-declarative-2to3/ (master*) $ ./test-equal-range.sh                                                         [21:41:23]

real    0m1.743s
user    0m12.628s
sys     0m0.520s
{
  "number_of_files": 115,
  "lines_of_code": 55648,
  "number_of_matches": 14,
  "total_time": 1125.8220672607422
}Diffs
```
