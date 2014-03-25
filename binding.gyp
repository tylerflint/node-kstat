{
  'targets': [
    {
      'target_name': 'kstat',
      'sources': [ 'kstat.cc' ],
      'libraries': [ '-lkstat', '-lavl', '-lcmdutils', '-ldevinfo', '-lgen', '-lc', '-lnvpair', '-lsec', '-lnsl', '-lidmap', '-lmp', '-lmd', '-luutil', '-lm'],
      'cflags_cc': [ '-Wno-write-strings' ],
      'cflags_cc!': [ '-fno-exceptions' ],
    }
  ]
}
