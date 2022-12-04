from tabulate import tabulate
import time

records = [
  {'Customer Name': 'James', 'Package Name': 'Deluxe', 'Total Cost': 600, 'NoPax': 2},
  {'Customer Name': 'Adam', 'Package Name': 'VIP', 'Total Cost': 300, 'NoPax': 5},
  {'Customer Name': 'Mary', 'Package Name': 'Economy', 'Total Cost': 140, 'NoPax': 3},
  {'Customer Name': 'Clark', 'Package Name': 'Business', 'Total Cost': 120, 'NoPax': 1},
  {'Customer Name': 'Wendy', 'Package Name': 'Standard', 'Total Cost': 200, 'NoPax': 8},
  {'Customer Name': 'Jacky', 'Package Name': 'Premium', 'Total Cost': 260, 'NoPax': 4},
  {'Customer Name': 'Xavier', 'Package Name': 'Travel', 'Total Cost': 330, 'NoPax': 3},
  {'Customer Name': 'Bernard', 'Package Name': 'VVIP', 'Total Cost': 560, 'NoPax': 6},
  {'Customer Name': 'Prakash', 'Package Name': 'Individual', 'Total Cost': 420, 'NoPax': 7},
  {'Customer Name': 'Robert', 'Package Name': 'Deluxe', 'Total Cost': 150, 'NoPax': 1},
]

cust_list = []
package_list = []
pax_list = []

MENU =  "Hello, what would you like to perform?\n\n"\
        "1. Display all records\n"\
        "2. Sort record by Customer Name\n"\
        "3. Sort reord by Package Name\n"\
        "4. Sort record by Total Cost\n"\
        "5. Search record by Customer Name\n"\
        "6. Search record by Package Name\n"\
        "7. List records range from $X to $Y\n"\
        "8. Sort record by Pax Number\n"\
        "9. Sort record by Customer Name\n"\
        "10. Search record by Pax Number\n"\
        "0. Exit application\n"

Update_Menu = "Hello, what would you like to update?\n\n"\
              "1. Update Customer Name\n"\
              "2. Update Package Name\n"\
              "3. Update Total Cost\n"\
              "4. Update Number of Pax\n"\
              "0. Save update and return to main menu\n"


def displayRecords(records=records):
  print(tabulate(records, headers='keys', tablefmt="rst"))


def resume():
  while True:
    choice = input('Return to Main Menu (Y/N)?: ')
    try:
      choice = str(choice)
      if choice.upper() == 'Y':
        return
      elif choice.upper() == 'N':
        quit('Thank You! Have a Nice Day!!')
      else:
        print('Invalid Input!')
    except ValueError:
      print('Invalid')


def confirm():
  while True:
    option = input('Are You Sure? (Y/N): ')
    try:
      option = str(option)
      if option.upper() == 'Y':
        return
      elif option.upper() == 'N':
        update()
      else:
        print('Invalid Input')
    except ValueError:
      print('Invalid Value')

def update():
  while True:
    print(Update_Menu)
    option = input('>')
    try:
      option = int(option)
      if option == 1:
        for a in range(len(cust_list)):
          new = input('New Customer Name: ')
          cust_list[a]["Customer Name"] = new
          print('Customer Name updated')
          displayRecords(cust_list)
      elif option == 2:
        for a in range(len(cust_list)):
          new = input('New Package Name: ')
          cust_list[a]["Package Name"] = new
          print('Package Name updated')
          displayRecords(cust_list)
      elif option == 3:
        for a in range(len(cust_list)):
          new = input('New Total Cost: ')
          cust_list[a]["Total Cost"] = new
          print('Total Cost updated')
          displayRecords(cust_list)
      elif option == 4:
        for a in range(len(cust_list)):
          new = input('New Pax Number: ')
          cust_list[a]["NoPax"] = new
          print('Number of Pax updated')
          displayRecords(cust_list)
      elif option == 0:
        cust_list.clear()
        package_list.clear()
        confirm()
        break
      print('Invalid Input')
    except ValueError:
      print('Invalid Value')


def bubbleSort(records):
  n = len(records)
  for i in range(n - 1):
    swapped = False
    for j in range(0, n - i - 1):
      if records[j]['Customer Name'] > records[j + 1]['Customer Name']:
        records[j], records[j + 1] = records[j + 1], records[j]
        swapped = True
    if swapped == False:
      break
  print('Records sorted by Customer Name')
  displayRecords()


def selectionSort(records):
  for i in range(len(records)):
    min_idx = i
    for j in range(i + 1, len(records)):
      if records[min_idx]['Package Name'] > records[j]['Package Name']:
        min_idx = j
    records[i], records[min_idx] = records[min_idx], records[i]
  print('Records sorted by Package Name')
  displayRecords()


def insertionSort(records):
  for i in range(1, len(records)):
    key = records[i]
    j = i - 1
    while j >= 0 and key['Total Cost'] < records[j]['Total Cost']:
      records[j + 1] = records[j]
      j -= 1
    records[j + 1] = key
  print('Records sorted by Total Cost')
  displayRecords()


def packageSort(records):
  for i in range(1, len(records)):
    key = records[i]
    j = i - 1
    while j >= 0 and key['Package Name'] < records[j]['Package Name']:
      records[j + 1] = records[j]
      j -= 1
    records[j + 1] = key

#Additional Feature - Sort Number of Pax using Shell Sort
def shellSort(records):
  n = len(records)
  gap = n // 2
  while gap > 0:
    j = gap
    # Check the array in from left to right
    # Till the last possible index of j
    while j < n:
      i = j - gap  # This will keep help in maintain gap value
      while i >= 0:
        # If value on right side is already greater than left side value
        # We don't do swap else we swap
        if records[i + gap]['NoPax'] > records[i]['NoPax']:
          break
        else:
          records[i + gap], records[i] = records[i], records[i + gap]
        i = i - gap  # To check left side also
        # If the element present is greater than current element
      j += 1
    gap = gap // 2
  print('Records sorted by Number of Pax')
  displayRecords()

def heapify(records, n, i):
  largest = i # Initialize largest as root
  l = 2 * i + 1	 # left = 2*i + 1
  r = 2 * i + 2	 # right = 2*i + 2

  # See if left child of root exists and is
  # greater than root
  if l < n and records[largest]['NoPax'] < records[l]['NoPax']:
      largest = l

  # See if right child of root exists and is
  # greater than root
  if r < n and records[largest]['NoPax'] < records[r]['NoPax']:
      largest = r

  # Change root, if needed
  if largest != i:
      records[i], records[largest] = records[largest], records[i] # swap

      # Heapify the root.
      heapify(records, n, largest)

# The main function to sort an array of given size
def heapSort(records):
  n = len(records)

  # Build a maxheap.
  for i in range(n//2 - 1, -1, -1):
      heapify(records, n, i)

  # One by one extract elements
  for i in range(n-1, 0, -1):
      records[i], records[0] = records[0], records[i] # swap
      heapify(records, i, 0)

#Addtional Feature - Sort Customer Name using Stooge Sort
def stoogesort(records, l, h):
  if l >= h:
      return
  # If first element is smaller
  # than last, swap them
  if records[l]['Customer Name']>records[h]['Customer Name']:
      t = records[l]
      records[l] = records[h]
      records[h] = t
  # If there are more than 2 elements in
  # the array
  if h-l + 1 > 2:
      t = (int)((h-l + 1)/3)
      # Recursively sort first 2 / 3 elements
      stoogesort(records, l, (h-t))
      # Recursively sort last 2 / 3 elements
      stoogesort(records, l + t, (h))
      # Recursively sort first 2 / 3 elements
      # again to confirm
      stoogesort(records, l, (h-t))

def linearSearch(records):
  while True:
    name = input('Search Customer Name: ')
    for i in range(len(records)):
      if (records[i]['Customer Name'] == name):
        cust_list.append(records[i])
        displayRecords(cust_list)
        update()
        return
    print("Customer not found.")


def binarySearch(records):
  low = 0
  high = len(records) - 1
  while True:
    target= input('Search Package Name:')
    while low <= high:
        mid = (low + high) // 2
        if target == records[mid]['Package Name']:
          package_list.append(records[mid])
          displayRecords(package_list)
          update()
          return
        elif records[mid]['Package Name'] < target:
            low = mid + 1
        elif records[mid]['Package Name'] > target:
            high = mid - 1
    return 'Package Not Found'

def interpolationSearch(records, lo, hi, x):

  # Since array is sorted, an element present
  # in array must be in range defined by corner
  while lo <= hi and x >= records[lo]['NoPax'] and x <= records[hi]['NoPax']:

      # Probing the position with keeping
      # uniform distribution in mind.
      pos = lo + ((hi - lo) // (records[hi]['NoPax'] - records[lo]['NoPax']) *
                  (x - records[lo]['NoPax']))

      # Condition of target found
      if records[pos]['NoPax'] == x:
          pax_list.append(records[pos])
          return pos

      # If x is larger, x is in right subarray
      if records[pos]['NoPax'] < x:
          return interpolationSearch(records, pos + 1,
                                  hi, x)

      # If x is smaller, x is in left subarray
      if records[pos]['NoPax'] > x:
          return interpolationSearch(records, lo,
                                  pos - 1, x)
  return -1



def listRecords(records):
  while True:
    try:
      range_from = float(input('From: $'))
      range_to = float(input('To: $'))
      filtered_records = []
      for record in records:
        if range_from <= record['Total Cost'] <= range_to:
          filtered_records.append(record)
          displayRecords(filtered_records)
          break
        elif range_from >= record['Total Cost'] or range_to <= record['Total Cost']:
          return "Incorrect Cost Range"
    except ValueError:
      return 'Please enter Valid Cost.'


while True:
    print(MENU)
    option = input('-->')
    try:
      option = int(option)
      if option == 1:
        displayRecords()
        time.sleep(1)
      elif option == 2:
        bubbleSort(records)
        time.sleep(0.5)
        resume()
      elif option == 3:
        selectionSort(records)
        time.sleep(0.5)
        resume()
      elif option == 4:
        insertionSort(records)
        time.sleep(0.5)
        resume()
      elif option == 5:
        linearSearch(records)
        time.sleep(0.5)
        resume()
      elif option == 6:
        packageSort(records)
        print(binarySearch(records))
        time.sleep(0.5)
        resume()
      elif option == 7:
        listRecords(records)
        time.sleep(0.5)
        resume()
      elif option == 8:
        shellSort(records)
        time.sleep(0.5)
        resume()
      elif option == 9:
        n = len(records)
        stoogesort(records, 0, n - 1)
        displayRecords(records)
        time.sleep(0.5)
        resume()
      elif option == 10:
        n = len(records)
        heapSort(records)
        index = interpolationSearch(records, 0, len(records) - 1, int(input('Enter Number: ')))
        if index != -1:
          displayRecords(pax_list)
          update()
          time.sleep(0.5)
          resume()
        else:
          print("Element not found")
      elif option == 0:
        quit('Thank You! Goodbye')
      else:
        print('Invalid option.\n')
    except ValueError:
      print('Please Enter Valid Value')
