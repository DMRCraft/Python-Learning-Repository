# Format specifiers - special instruction withing a f string that formats a value based on what flags are inserted

{variable:specifier}

## Note: in (number), dont include the brackets!

- .(number)f = round to that many decimal places
- :(number) = allocate that many spaces
- :0(number) = allocate and zero pad that many spaces
- :< = left justify
- :> = right justify
- :^ = center align
- :+ = use a plus sign to indicate positive value
- := = place sign to leftmost position
- : = insert a space before positive numbers
- :, = comma separator
- :% = percentage format
