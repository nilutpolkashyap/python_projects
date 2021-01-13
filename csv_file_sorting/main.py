     import sys, csv ,operator
      data = csv.reader(open('File.csv'),delimiter=',')
      sortedlist = sorted(data, key=operator.itemgetter(0))    # 0 specifies according to first column we want to sort
      #now write the sorte result into new CSV file
      with open("NewFile.csv", "wb") as f:
          fileWriter = csv.writer(f, delimiter=',')
          for row in sortedlist:
              fileWriter.writerow(row)
