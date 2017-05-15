#!/usr/bin/perl -w
#----------------------------------------------------------------------------------
# Title     : script-1.pl
# Function  : Reads in multiple gene sequences in FASTA format and runs blast for each entry against chosen database 
# Version   : 1.0
# Comments  : Kogenaru et al. Repertoire of novel sequence signatures for the detection of Candidatus Liberibacter asiaticus by quantitative real-time PCR
#----------------------------------------------------------------------------------
use strict;

# Global variables
my $options = "";                    # users input options
my $infile = "";                     # input fasta file
my $dbfile = "";                     # database file to search
my $instring = "";                   # put infile in one string
my @inarray = "";                    # store each entry in array
my %unique=();                       # unique names
my $help = '
Read in the input FASTA file containing multiple entries and run blast for each 
entry against database specified.
The blast options are hard coded in the script
usage: script-1.pl -i <file containing multiple gene sequence in FASTA format> -d 
<database file in fastaformat>
Example: script-1.pl -i Las.fa -d nt.fa
';

# Processing command line options
if (@ARGV<1) {die $help;}
# if input file is given without -i option: insert -i before the file name
if ($ARGV[0]!~/^-/) {unshift(@ARGV,"-i");}
foreach my $argv (@ARGV){
    $options .= "$argv ";
} #-- end of foreach loop
# Set options
if ($options =~ s/-i\s+(\S+)//g) {$infile = $1;}
if ($options =~ s/-d\s+(\S+)//g) {$dbfile = $1;}
# Warn if unknown options found
if ($options !~ /^\s*$/) {
    $options =~ s/^\s*(.*?)\s*$/$1/g; 
    printf ("WARNING: unknown options '$options'\n");
} #-- end of if loop
# Extra safety
if ($infile eq "" && $dbfile eq "") {die $help;}
# Handling the input file
open (IN, "<$infile") || die ("WARNING: could not open the $infile: $!\n");
while (defined(my $inline = <IN>)){ # retrieve file,line by line
    $instring .= $inline;           # append lines
} #-- End of the second  while loop
    close (IN);
@inarray = split(/>/, $instring);   # split on fasta > character
shift (@inarray);                   # removes the empty element
my $seq_nr = @inarray;
my $count = 0;
my $entry_name = ""; # each entry name
# print number of sequence found in the input multifasta file
printf(STDERR "\nFound %i sequences in the input file: %s\n\n",$seq_nr,$infile);
foreach  my $seq (@inarray) {              # split each seq 
#>ref|NC_012985.2|:36-407 hypothetical protein CLIBASIA_00005 [Candidatus Liberibacter asiaticus str. psy62]
    if ($seq =~/^\s*(\w+)\|(\w+).(\d+)\|:([-\w+]+)/){ #110703 MK
$entry_name = $4;
$unique{$4}="defined"; #110704 mk
    } #--  if ($seq =~
    my $tempin = "$entry_name" . ".seq";
    my $blastout = "$entry_name" . ".blast";
    open(TMP,">$tempin") or die ("WARNING: could not write $tempin: $!\n");
    printf (TMP ">$seq");  # write the entry into temp file for blast
    close (TMP);
# calling blast program: blastall -p blastn -d dbfile -i infile -o outfile -a 10
    &syscall (" blastall -p blastn -d $dbfile -i $tempin -o $blastout -e 1e-3 -a 
10"); #110707 sk
    $count++;
    printf(STDERR "BLAST searches done for %i of %i\n",$count,$seq_nr);
    &syscall ("rm -rf $tempin");
} #-- end of foreach my $seq
# count unique sequence file names found
my @keys = keys %unique;
my $size = @keys;
printf(STDERR "\nFound %i unique sequences in the input file: 
%s\n\n",$size,$infile);
printf(STDERR "\nSearching done!....\n\n");
# subroutine to call system commands
sub syscall {
    my $cmd=$_[0];
    printf("exec: '$cmd'\n"); 
    return system($cmd)/256; 
}
