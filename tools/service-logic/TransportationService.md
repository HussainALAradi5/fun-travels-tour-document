## Business logic

- Lists, search, and detail are for staff: agency staff see only their agency's vehicles, admins all. Customers get 403. Search matches provider, internal code, and registration number.
- A missing vehicle is 404. Agency staff always create vehicles in their own agency; a branch must belong to that agency. Codes are unique, and a registration number is unique per provider.
- Seats are generated from the capacity and `seatConfig` (special chair counts; the rest are standard). Editing re-labels chair types only while no booking or running tour locks the layout.
