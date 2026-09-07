# PaymentProcessingService

**File:** `src/main/java/com/server/server/services/Account/PaymentProcessingService.java`

## Code

```java
@Transactional
public TourReservation processCheckout(TourReservation reservation, PaymentMethod chosenMethod, String externalTransactionId) {
    BigDecimal amountDue = reservation.getTotalPrice();
    boolean isPaid = false;

    if (chosenMethod == PaymentMethod.WALLET) {
        Account userAccount = accountService.getAccountByUserId(reservation.getUser().getId());
        transactionService.debitAccount(userAccount, amountDue, TransactionType.PAYMENT, "Paid for Tour: " + reservation.getReservationNumber(), reservation);
        isPaid = true;
    } else if (chosenMethod == PaymentMethod.CREDIT_CARD || chosenMethod == PaymentMethod.PAYPAL) {
        Payment payment = Payment.builder()
                .method(chosenMethod)
                .transactionId(externalTransactionId)
                .amount(amountDue)
                .status(PaymentStatus.COMPLETED)
                .reservation(reservation)
                .build();
        paymentRepository.save(payment);
        isPaid = true;
    } else if (chosenMethod == PaymentMethod.BANK_TRANSFER || chosenMethod == PaymentMethod.CASH_AT_OFFICE) {
        reservation.setStatus(GenericStatus.PENDING);
    }

    if (isPaid && reservation.getStatus() == GenericStatus.PENDING) {
        reservation.setStatus(GenericStatus.CONFIRMED);
        tourService.restoreInventory(reservation.getTour().getId(), -reservation.getRequestedSlots());
        if (reservation.getTickets() != null) {
            for (Ticket ticket : reservation.getTickets()) {
                ticket.setTicketStatus(TicketStatus.CONFIRMED);
                ticket.setApprovalStatus(GenericStatus.APPROVED);
                if (ticket.getAssignedSeat() != null) {
                    seatService.updateStatus(ticket.getAssignedSeat().getId(), SeatStatus.BOOKED);
                }
            }
        }
    }
    return reservationRepository.save(reservation);
}
```

## Methods

### processCheckout(reservation, chosenMethod, externalTransactionId) -> TourReservation

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| reservation | TourReservation | Reservation to pay for |
| chosenMethod | PaymentMethod | WALLET, CREDIT_CARD, PAYPAL, BANK_TRANSFER, CASH_AT_OFFICE |
| externalTransactionId | String | Stripe/PayPal transaction ID |

**Returns:** Updated TourReservation

**Business Logic:**
1. **WALLET:** Debits user account via TransactionService
2. **CREDIT_CARD/PAYPAL:** Creates Payment record with COMPLETED status
3. **BANK_TRANSFER/CASH:** Sets reservation to PENDING (manual confirmation needed)
4. If paid and reservation was PENDING:
   - Sets reservation to CONFIRMED
   - Decreases tour available slots
   - Confirms all tickets
   - Locks assigned seats (sets to BOOKED)

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | Insufficient balance (wallet) |
| RuntimeException | Stripe/Card errors |
