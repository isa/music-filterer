require 'rake/clean'

directory 'data'
CLOBBER.include('data')

task :default => :migrate

task :migrate => 'data' do
   sh 'sqlite3 data/library.db < library.sql'
end
