include version.txt config.mk

#include config.mk version.txt

all: build

build:
	echo "Building project with version $(VERSION)"

clean:
	rm -rf *.o

# New target for foo
foo:
	frobnicate > foo

# Pattern rule for any target that isn't defined
#%: force
#	@$(MAKE) -f Makefile $@

#force: ;

if-app-change:
	@echo "Running app regardless of changes..."
	python ./myapp2/app2.py

if-app-change2: ./myapp2/app2.py
	@echo "Running app only if app2.py has changed..."
	python ./myapp2/app2.py

files := file1 file2
some_file: $(files)
	echo "Look at this variable: " $(files)
	touch some_file

file1:
	touch file1
file2:
	touch file2

clean1:
	rm -f file1 file2 some_file

# Deferred assignment: value is evaluated when 'var1' is used
var1 = $(var2)
var2 = deferred_value

# Conditional assignment: 'var3' will be set to 'conditional_value' only if it's not already set
var3 ?= conditional_value

# Immediate assignment: value is evaluated at the time of assignment
var4 := $(var5)
var5 = immediate_value

# Append assignment: adds value to an existing variable
var6 = initial_value
var6 += appended_value

# Shell assignment: runs a shell command and assigns its output
var7 != echo shell_value

all_var:
	@echo "Deferred assignment (var1): $(var1)"  # Prints 'deferred_value'
	@echo "Conditional assignment (var3): $(var3)"  # Prints 'conditional_value'
	@echo "Immediate assignment (var4): $(var4)"  # Prints empty because 'var5' wasn't set at the time of assignment
	@echo "Append assignment (var6): $(var6)"  # Prints 'initial_value appended_value'
	@echo "Shell assignment (var7): $(var7)"  # Prints 'shell_value'

all_is: f1.o f2.o  # 'all' depends on f1.o and f2.o

# Rule for generating f1.o and f2.o
f1.o f2.o:
	@echo "This target is: $@"  # $@ will print the name of the target being built (either f1.o or f2.o)
	@touch $@  # Simulates creating the target file (f1.o or f2.o)

# Clean up rule to delete generated .o files
clean_is:
	@rm -f f1.o f2.o
	@echo "Cleaned up .o files"

# Print out file information about every .c file
print: $(wildcard *.txt)
	@echo "Changed or new files:"
	@ls -la $?  # $^ expands to all dependencies, which are all the .txt files
