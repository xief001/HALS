### Overview
HALS is software that makes self-correction for long reads with high throughput.

### Copy right
HALS is under the [Artistic License 2.0](http://opensource.org/licenses/Artistic-2.0).

### Short manual
1. System requirements

   HALS is suitable for 32-bit or 64-bit machines with Linux operating systems. At least 4GB of system memory is recommended for correcting larger data sets.

2. Installation

   The MECAT self-correction and assembly software is required to run HALS.
   * The source files in 'src' folder can be complied to generate a 'bin' folder by running Makefile: make all.
   * Put MECAT and the 'bin' folder to your $PATH: export PATH=PATH2MECAT:$PATH and export PATH=PATH2bin:$PATH, respectively.

3. Inputs
   * Long reads in FASTA format.
   
4. Using HALS

   ```
   HALS long_reads.fasta [-options|-options]
   ```

   <p>Options (default value):<br>
   -f1 (0.5)<br>
   Fraction value to distinguish between the cases (i)/(ii) and (iii).<br>
   -f2 (0.5)<br>
   Fraction value to distinguish between the cases (i) and (ii).<br>
   -d1 (0.05)<br>
   Difference value of alignment identities to find the correct aligned path.<br>
   -d2 (0.2)<br>
   Difference value of expected amounts of aligned long reads to find the correct aligned path.<br>

      
5. Outputs
   * Error corrected full long reads.
   * Error corrected trimmed long reads.
   * Error corrected split long reads.


